from __future__ import absolute_import

import xml
from xml.dom.minidom import parseString
import requests
from pythesint.json_vocabulary import JSONVocabulary


class CFVocabulary(JSONVocabulary):
    def _fetch_online_data(self):
        # Note the version number... Would probably be better to make it always
        # take the last version..
        try:
            r = requests.get(self.url)
        except requests.RequestException:
            print("Could not get the vocabulary file at '{}'".format(self.url))
            raise
        dom = parseString(r.text.encode('utf-8').strip())
        # should only contain the standard_name_table:
        node = dom.childNodes[0]

        details = {}
        metadata_details = node.getElementsByTagName('owl:Ontology')[0]
        for detail in metadata_details.childNodes:
            if type(detail)==xml.dom.minidom.Element:
                details[detail.nodeName] = detail.childNodes[0].data

        cf_list = [details]
        for cnode in node.getElementsByTagName('Standard_Name')[0].childNodes:
            if type(cnode)==xml.dom.minidom.Element:
                entry = cnode.getElementsByTagName('Standard_Name')[0]
                standard_name = entry.getAttribute('rdf:about')
                units = ''
                if entry.getElementsByTagName('canonical_units'):
                    units = entry.getElementsByTagName(
                        'canonical_units')[0].childNodes[0].nodeValue
                if entry.getElementsByTagName('skos:definition'):
                    definition = entry.getElementsByTagName(
                            'skos:definition')[0].childNodes[0].nodeValue
                stdname = {
                    'standard_name': standard_name,
                    'canonical_units': units,
                    'definition': definition
                }
                cf_list.append(stdname)
        return cf_list

