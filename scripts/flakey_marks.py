#!/usr/bin/env python
"""
Produces a list of tests which have the `flaky` marker applied
to them.
"""
import json
import subprocess
import xml.etree.ElementTree as ET
from tempfile import NamedTemporaryFile


ret = {'flaky_test_markers': []}

tmp_xml = NamedTemporaryFile(delete=True)

subprocess.run(['pytest', '--setup-plan', '-m', 'flaky', '--junit-xml={}'.format(tmp_xml.name)], capture_output=True)
tree = ET.parse(tmp_xml)
root = tree.getroot()

for child in root.findall('./testsuite/testcase'):
    if not list(child):
        ret['flaky_test_markers'].append((child.attrib))
print(json.dumps(ret))
