import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'agency')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_observation_channels_and_coverage_changes_are_retained(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        self.assertEqual({row['version'] for row in data['catalogs']['instruments']}, {'v1', 'v2'})
        kinds = {row['kind'] for row in data['records']}
        self.assertTrue({'survey-response', 'written-reflection', 'observation', 'opportunity-coverage', 'channel-change', 'observation-plan'} <= kinds)
        coverage = next(row for row in data['records'] if row['kind'] == 'opportunity-coverage')
        self.assertGreater(coverage['eligible'], coverage['observed'])

if __name__ == '__main__':
    unittest.main()
