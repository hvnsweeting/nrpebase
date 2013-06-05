{{ '{#' }}
 Diamond statistics for {{ app }}
{{ '#}' }}

include:
  - diamond
{{ app }}_diamond_collector:
  file:
    - managed
    - name: /etc/diamond/collectors/{{ app.capitalize() }}Collector.conf
    - template: jinja
    - user: root
    - group: root
    - mode: 440
    - source: salt://{{ app }}/diamond/config.jinja2
    - context:
      instances: {{ '{{' }} pillar['{{ app }}']|default({}) {{ '}}' }}
    - require:
      - file: /etc/diamond/collectors

{{ app }}_diamond_resources:
  file:
    - accumulated
    - name: processes
    - filename: /etc/diamond/collectors/ProcessResourcesCollector.conf
    - require_in:
      - file: /etc/diamond/collectors/ProcessResourcesCollector.conf
    - text:
      - |
        [[{{ app }}]]
        exe = ^\/usr\/sbin\/{{ app }}$

extend:
  diamond:
    service:
      - watch:
        - file: {{ app }}_diamond_collector
