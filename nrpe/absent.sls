{{ '{#' }}
 Remove Nagios NRPE check for {{ app }}
{{ '#}' }}


{{ "{% if 'shinken_pollers' in pillar %}" }}
include:
  - nrpe

extend:
  nagios-nrpe-server:
    service:
      - watch:
        - file: /etc/nagios/nrpe.d/{{ app }}.cfg
{{ '{% endif %}' }}

/etc/nagios/nrpe.d/{{ app }}.cfg:
  file:
    - absent
