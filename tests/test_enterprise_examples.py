"""End-to-end checks of the shipped, source-backed research examples."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'skills' / 'dejiny-podniku-a-remesla' / 'scripts' / 'badatel.py'
EXAMPLES = (
    'uhersky-brod-cz.json',
    'plzen-skoda.json',
    'pribram-drtikol.json',
)


class PublishedExamplesTest(unittest.TestCase):
    def call_cli(self, *arguments):
        result = subprocess.run(
            [sys.executable, str(CLI), *map(str, arguments)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_all_research_examples_validate_and_keep_evidence_in_html(self):
        for filename in EXAMPLES:
            with self.subTest(example=filename), tempfile.TemporaryDirectory() as tmp:
                path = ROOT / 'examples' / filename
                data = json.loads(path.read_text(encoding='utf-8'))
                self.call_cli('validate', path)
                rendered = Path(tmp) / 'report.html'
                self.call_cli('render', path, '--format', 'html', '--out', rendered)
                html = rendered.read_text(encoding='utf-8')
                self.assertIn(data['project']['title'], html)
                for source in data['sources']:
                    self.assertIn(source['url'], html)
                for claim in data['claims']:
                    self.assertIn(claim['text'], html)

    def test_unlocated_historical_workshops_do_not_get_invented_coordinates(self):
        for filename in EXAMPLES:
            with self.subTest(example=filename), tempfile.TemporaryDirectory() as tmp:
                rendered = Path(tmp) / 'places.geojson'
                self.call_cli('render', ROOT / 'examples' / filename,
                              '--format', 'geojson', '--out', rendered)
                data = json.loads(rendered.read_text(encoding='utf-8'))
                self.assertEqual(data['type'], 'FeatureCollection')
                self.assertEqual(data['features'], [])


if __name__ == '__main__':
    unittest.main()
