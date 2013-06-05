{{ '{#' }}
 Turn off Diamond statistics for {{ app }}
{{ '#}' }}
{{ "{% if 'graphite_address' in pillar %}" }}
include:
  - diamond

extend:
  diamond:
    service:
      - watch:
        - file: /etc/diamond/collectors/{{ app.capitalize() }}Collector.conf
{{ '{% endif %}' }}

/etc/diamond/collectors/{{ app.capitalize() }}Collector.conf:
  file:
    - absent
