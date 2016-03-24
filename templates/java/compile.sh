{% extends 'base/compile.sh' %}

{% block compile %}
javac ${CODE_DIR}/Main.java -d ${CODE_DIR} -cp ${CODE_DIR} 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
{% endblock %}