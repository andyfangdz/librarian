{% extends 'base/run.sh' %}

{% block run %}
python ${CODE_DIR}/Main.py ${INPUT_DIR}/{{ data_id }}.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
{% endblock %}
