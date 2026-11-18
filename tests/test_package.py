from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class PackageTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.skill = Path(temp.name) / 'skills' / 'pstack'
        shutil.copytree(REPO / 'skills' / 'pstack', self.skill)

    def check(self):
        return subprocess.run([sys.executable, '-B', str(self.skill / 'scripts/check-port.py')],
                              capture_output=True, text=True, timeout=10)

    def test_installed_copy_is_self_contained(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('22 playbooks, 34 specialists, 24 principles', result.stdout)
        self.assertEqual((REPO / 'LICENSE').read_bytes(),
                         (self.skill / 'references/LICENSE.txt').read_bytes())

    def test_broken_route_fails_closed(self):
        path = self.skill / 'references/engineering.md'
        path.write_text(path.read_text(encoding='utf-8').replace('## bug-fix', '## broken'),
                        encoding='utf-8')
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Route bug-fix lacks a unique section', result.stderr)

    def test_missing_license_fails_closed(self):
        (self.skill / 'references/LICENSE.txt').unlink()
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Missing upstream license', result.stderr)
