from __future__ import absolute_import

import urllib2
from xml.dom.minidom import parse

from pythesint.json_thesaurus import  JSONThesaurus

class CFThesaurus(JSONThesaurus):
    url = 'http://cfconventions.org/Data/cf-standard-names/30/src/cf-standard-name-table.xml'
    def __init__(self, name):
        self.name = name

    def _fetch_data(self):
        # Note the version number... Would probably be better to make it always
        # take the last version..
        u1 = urllib2.urlopen(self.url)
        dom = parse(u1)
        node = dom.childNodes[0] # should only contain the standard_name_table

        cf_list = []
        for entry in node.getElementsByTagName('entry'):
            standard_name = entry.attributes['id'].value
            units = ''
            if entry.getElementsByTagName(
                    'canonical_units')[0].childNodes:
                units = entry.getElementsByTagName(
                    'canonical_units')[0].childNodes[0].nodeValue
            grib = ''
            if entry.getElementsByTagName('grib')[0].childNodes:
                grib = entry.getElementsByTagName(
                    'grib')[0].childNodes[0].nodeValue
            amip = ''
            if entry.getElementsByTagName('amip')[0].childNodes:
                amip = entry.getElementsByTagName(
                    'amip')[0].childNodes[0].nodeValue
            desrc = ''
            if entry.getElementsByTagName('description')[0].childNodes:
                descr = entry.getElementsByTagName(
                    'description')[0].childNodes[0].nodeValue
            stdname = {
                    'standard_name': standard_name,
                    'canonical_units': units,
                    'grib': grib,
                    'amip': amip,
                    'description': descr
                }
            cf_list.append(stdname)
        return cf_list


CF_STANDARD_NAMES = 'cf_standard_names'

thesauri = {
    CF_STANDARD_NAMES : CFThesaurus(CF_STANDARD_NAMES),
}

def get_standard_name(item):
    return thesauri[CF_STANDARD_NAMES].find_keyword(item)

