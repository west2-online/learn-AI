#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const repoRoot = process.cwd();
const defaultTargets = ['README.md', 'tasks(2026)'];
const rawTargets = process.argv.slice(2);
const targets = rawTargets.length > 0 ? rawTargets : defaultTargets;
const excludedParts = new Set(['.git', '.venv', 'node_modules']);

function hasExcludedPart(filePath) {
  return filePath.split(path.sep).some((part) => excludedParts.has(part));
}

function collectMarkdownFiles(target) {
  const absolute = path.resolve(repoRoot, target);
  if (!fs.existsSync(absolute)) {
    throw new Error(`Path does not exist: ${target}`);
  }

  const stat = fs.statSync(absolute);
  if (stat.isFile()) {
    return absolute.toLowerCase().endsWith('.md') && !hasExcludedPart(absolute) ? [absolute] : [];
  }

  const files = [];
  const entries = fs.readdirSync(absolute, { withFileTypes: true });
  for (const entry of entries) {
    const child = path.join(absolute, entry.name);
    if (hasExcludedPart(child)) {
      continue;
    }
    if (entry.isDirectory()) {
      files.push(...collectMarkdownFiles(child));
    } else if (entry.isFile() && child.toLowerCase().endsWith('.md')) {
      files.push(child);
    }
  }
  return files;
}

function uniqueFiles(files) {
  return [...new Map(files.map((file) => [path.resolve(file), path.resolve(file)])).values()]
    .sort((left, right) => left.localeCompare(right));
}

function stripIgnoredInlineText(line) {
  return line
    .replace(/`[^`]*`/g, '')
    .replace(/!\[((?:[^\]\\]|\\.)*)\]\([^)]*\)/g, '')
    .replace(/\[((?:[^\]\\]|\\.)*)\]\([^)]*\)/g, '$1')
    .replace(/<https?:\/\/[^>]+>/g, '')
    .replace(/https?:\/\/\S+/g, '')
    .replace(/^\s*\d+\.\s+/, '');
}

const typographyRules = [
  {
    name: '中英文之间需要空格',
    pattern: /[\u4e00-\u9fff][A-Za-z][A-Za-z0-9+#]*|[A-Za-z0-9+#][\u4e00-\u9fff]/u,
  },
  {
    name: '中文与数字之间需要空格',
    pattern: /[\u4e00-\u9fff]\d|\d[\u4e00-\u9fff]/u,
  },
  {
    name: '数字与单位之间不需要空格',
    pattern: /\b\d+\s+(?:GB|MB|KB|TB|%|px|ms|kg|g|m|cm|mm)\b/iu,
  },
  {
    name: '中文语境使用全角标点',
    pattern: /[\u4e00-\u9fff][,!?;:]|[,!?;:][\u4e00-\u9fff]|[A-Za-z0-9)][,!?;:]\s*[\u4e00-\u9fff]/u,
  },
];

function checkTypography(files) {
  const issues = [];
  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const lines = content.split(/\r?\n/);
    let inFence = false;

    lines.forEach((line, index) => {
      if (/^\s*(```|~~~)/.test(line)) {
        inFence = !inFence;
        return;
      }
      if (inFence) {
        return;
      }

      const scanLine = stripIgnoredInlineText(line);
      for (const rule of typographyRules) {
        const match = scanLine.match(rule.pattern);
        if (match) {
          issues.push({ file, line: index + 1, rule: rule.name, match: match[0], text: line });
          break;
        }
      }
    });
  }
  return issues;
}

let markdownFiles;
try {
  markdownFiles = uniqueFiles(targets.flatMap(collectMarkdownFiles));
} catch (error) {
  console.error(error.message);
  process.exit(1);
}

if (markdownFiles.length === 0) {
  console.log('No Markdown files found.');
  process.exit(0);
}

console.log(`Checking ${markdownFiles.length} Markdown file(s).`);

const configPath = path.join(repoRoot, '.markdownlint.json');
const isWindows = process.platform === 'win32';
const npxCommand = isWindows ? 'npx.cmd' : 'npx';
const lintArgs = ['--yes', 'markdownlint-cli'];
if (fs.existsSync(configPath)) {
  lintArgs.push('-c', configPath);
}
lintArgs.push(...markdownFiles);

const lintResult = spawnSync(npxCommand, lintArgs, { stdio: 'inherit', shell: isWindows });
const lintFailed = lintResult.status !== 0;

const typographyIssues = checkTypography(markdownFiles);
if (typographyIssues.length > 0) {
  console.error('\nApple typography issues:');
  for (const issue of typographyIssues) {
    const relative = path.relative(repoRoot, issue.file);
    console.error(`${relative}:${issue.line}: ${issue.rule} [${issue.match}]`);
    console.error(`  ${issue.text}`);
  }
}

if (lintFailed || typographyIssues.length > 0) {
  process.exit(1);
}

console.log('Markdown checks passed.');
