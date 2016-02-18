from __future__ import absolute_import

import unittest
import os, json
#import doctest
#doctest.testfile('pythesint/pythesint.py')

from pythesint import pythesint, gcmd_keywords, cf_standard_names

class GetGCMDKeywordsTest(unittest.TestCase):

    def test_write_json(self):
        for list_name in pythesint.standard_lists.keys():
            pythesint.write_json(list_name)
            fn = os.path.join(pythesint.json_path,
                    pythesint.json_filename(list_name))
            dd = json.load(open(fn))
            self.assertIsInstance(dd, list)

    def test_write_json_to_path(self):
        gcmd_list = 'gcmd_instruments'
        path = 'tmp/json_test'
        with self.assertRaises(OSError):
            pythesint.write_json(gcmd_list, path=path)
        path = 'json_test'
        pythesint.write_json(gcmd_list, path=path)
        fn = os.path.join(path,
                    pythesint.json_filename(gcmd_list))
        dd = json.load(open(fn))
        self.assertIsInstance(dd, list)
        os.unlink(fn)
        os.rmdir(path)

    def test_find_instrument(self):
        self.assertIsInstance(gcmd_keywords.get_instrument('MODIS'), dict)
        self.assertIsInstance(pythesint.get_instrument('MODIS'), dict)

    def test_rewrite_json_and_find_instrument(self):
        self.assertIsInstance(gcmd_keywords.get_instrument('MODIS',
            update=True), dict)
        self.assertIsInstance(pythesint.get_instrument('MODIS',
            update=True), dict)

    def test_find_instrument_class(self):
        self.assertIsInstance(
                gcmd_keywords.get_instrument('active remote sensing'), 
                dict)
        self.assertIsInstance(
                pythesint.get_instrument('active remote sensing'), 
                dict)

    def test_find_science_keyword_term(self):
        self.assertIsInstance(
                gcmd_keywords.get_science_keyword('curriculum support'), dict)
        self.assertIsInstance(
                pythesint.get_science_keyword('curriculum support'), dict)

    def test_find_science_keyword(self):
        self.assertIsInstance(
                gcmd_keywords.get_science_keyword('sigma naught'), dict)
        self.assertIsInstance(
                pythesint.get_science_keyword('sigma naught'), dict)

    def test_find_platform(self):
        self.assertIsInstance(gcmd_keywords.get_platform('AQUA'), dict)
        self.assertIsInstance(pythesint.get_platform('AQUA'), dict)

    def test_find_iso_topic_category(self):
        self.assertIsInstance(gcmd_keywords.get_iso_topic_category('oceans'),
                str)
        self.assertIsInstance(pythesint.get_iso_topic_category('oceans'),
                str)

    def test_find_data_center(self):
        self.assertIsInstance(gcmd_keywords.get_data_center('NERSC'), dict)
        self.assertIsInstance(pythesint.get_data_center('NERSC'), dict)

    def test_find_location_category(self):
        self.assertIsInstance(gcmd_keywords.get_location('continent'), dict)
        self.assertIsInstance(pythesint.get_location('continent'), dict)

    def test_find_location_type(self):
        self.assertIsInstance(gcmd_keywords.get_location('africa'), dict)
        self.assertIsInstance(pythesint.get_location('africa'), dict)

    def test_find_location_subregion1(self):
        self.assertIsInstance(gcmd_keywords.get_location('central africa'), dict)
        self.assertIsInstance(pythesint.get_location('central africa'), dict)

    def test_find_location_subregion2(self):
        self.assertIsInstance(gcmd_keywords.get_location('Angola'), dict)
        self.assertIsInstance(pythesint.get_location('Angola'), dict)

    def test_find_location_subregion3(self):
        self.assertIsInstance(gcmd_keywords.get_location('HONG KONG'), dict)
        self.assertIsInstance(pythesint.get_location('HONG KONG'), dict)

    def test_find_cf_sar_nrcs(self):
        self.assertIsInstance(pythesint.get_cf_standard_name(
            'surface_backwards_scattering_coefficient_of_radar_wave'), dict)

    def test_unexisting_raises(self):
        with self.assertRaises(StandardError):
            pythesint.write_json('bullshit')