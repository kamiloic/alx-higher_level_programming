#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
	PyObject *str;

	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		str = PyUnicode_AsUTF8String(p);
		const char *value = PyBytes_AsString(str);

		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", value);

		Py_XDECREF(str);
	}
	else if (PyBytes_Check(p))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", PyBytes_GET_SIZE(p));
		printf("  value: %s\n", PyBytes_AsString(p));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
