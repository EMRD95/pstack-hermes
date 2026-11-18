"""Check pstack route integrity and optional pinned upstream name coverage."""
import argparse
from pathlib import Path
import re
import subprocess

PIN = '35a90942a7f02e1ebbc2443643179815f2147954'
ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references'


def names(path):
    return re.findall(r'^\| ([a-z-]+) \|', path.read_text(encoding='utf-8'), re.M)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream', type=Path, help='cursor/plugins checkout at the pinned revision')
    args = parser.parse_args()
    index = (REF / 'playbook-index.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| ([a-z-]+) \| `([a-z-]+\.md)` \|', index, re.M)
    routes = [route for route, _ in rows]
    specialists = names(REF / 'specialists.md')
    principles = ['principle-' + name for name in names(REF / 'principles.md')]
    for items, total in ((routes, 22), (specialists, 34), (principles, 24)):
        require(len(items) == total and len(set(items)) == total, 'Incorrect or duplicate entries')
    for route, file in rows:
        text = (REF / file).read_text(encoding='utf-8')
        require(text.splitlines().count(f'## {route}') == 1, f'Route {route} lacks a unique section')
    entry = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    for link in re.findall(r'`((?:references|templates)/[^`]+)`', entry):
        require((ROOT/link).is_file(), f'Missing reference: {link}')
    require((REF/'LICENSE.txt').is_file(), 'Missing upstream license')
    if args.upstream:
        head = subprocess.check_output(['git', '-C', str(args.upstream), 'rev-parse', 'HEAD'], text=True).strip()
        require(head == PIN, 'Wrong upstream revision')
        src = args.upstream / 'pstack'
        expected_routes = {p.stem for p in (src/'skills/poteto-mode/playbooks').glob('*.md')}
        expected_skills = {p.parent.name for p in (src/'skills').glob('*/SKILL.md')}
        require(set(routes) == expected_routes, 'Upstream route mismatch')
        require(set(specialists + principles) == expected_skills, 'Upstream skill mismatch')
        require((src/'LICENSE').read_bytes() == (REF/'LICENSE.txt').read_bytes(), 'License mismatch')
    print(f'PASS: {len(routes)} playbooks, {len(specialists)} specialists, {len(principles)} principles')


if __name__ == '__main__':
    main()
