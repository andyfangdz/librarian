{% extends 'base/run.sh' %}


{% block run %}
java -cp ${CODE_DIR} Main ${INPUT_DIR}/{{ data_id }}.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
{% endblock %}