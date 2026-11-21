import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'editions': ['edition', 'start', 'scope', 'class', 'label'], 'mapping': ['edition', 'legacy_class', 'candidate', 'condition'], 'register': ['item', 'period', 'source_edition', 'source_class', 'purpose', 'issuer'], 'signatures': ['id', 'item', 'edition', 'period', 'field', 'value', 'state', 'prior', 'at'], 'legacy_reports': ['report', 'period', 'edition', 'class', 'count', 'published_at'], 'rules': ['rule', 'edition', 'from_period', 'to_period', 'class', 'delta_pp', 'min_count', 'review_budget'], 'inquiries': ['id', 'rule', 'confirmed_at', 'evidence_cutoff']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
