from pathlib import Path
from unittest import TestCase

import bula


class ExportTest(TestCase):

    def test_environment(self):
        extensions = bula.ENVIRONMENT.get('extensions', [])
        self.assertIn('webassets.ext.jinja2.AssetsExtension', extensions)
        self.assertIn('jinja2.ext.with_', extensions)

    def test_filters(self):
        self.assertIn('images', bula.FILTERS)
        self.assertIs(bula.FILTERS['images'], bula.extract_images)
        self.assertIn('license', bula.FILTERS)
        self.assertIs(bula.FILTERS['license'], bula.generate_license)
        self.assertIn('schema', bula.FILTERS)
        self.assertIs(bula.FILTERS['schema'], bula.generate_jsonld_schema)

    def test_path(self):
        expected = str(Path(__file__).parent.parent.joinpath('bula'))
        self.assertEqual(bula.PATH, expected)
