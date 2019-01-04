import requests
import re
import natsort
import logging

def web_latest_version(url, version_regex):
    response = requests.get(url)
    response.raise_for_status()
    match_iter = re.finditer(version_regex, response.text, re.MULTILINE)
    version_set = set([m.group('version') for m in match_iter])
    if not len(version_set):
        raise exc.GetError(f'could not determine latest version based on input: '
                           f'url={repr(url)}, version_regex={repr(version_regex)}')
    latest_version = natsort.natsorted(list(version_set))[-1]
    return latest_version



languages = ["groovy", "flex", "java", "javascript", "php", "python", "typescript", "xml"]
version_regex=r'\>(?P<version>(\d+[^\/]+))'


for i in languages:
    u = f'https://dl.bintray.com/sonarsource/SonarQube/org/sonarsource/{i}/sonar-{i}-plugin'
    latest_version = web_latest_version(u, version_regex)
    print(i + ":" + latest_version)


scm = ["svn", "git"]
for i in scm:
    u = f'https://dl.bintray.com/sonarsource/SonarQube/org/sonarsource/scm/{i}/sonar-scm-{i}-plugin'
    plugin_name = f'sonar-scm-{i}-plugin'
    latest_version = web_latest_version(u, version_regex)
    print(i + ":" + latest_version)


    # binary_name = f'{plugin_name}-{latest_version}.jar'
    # binary_url = f'{u}/{latest_version}/{binary_name}'
    # print(binary_url)
