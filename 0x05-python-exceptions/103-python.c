#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to a PyObject (Python object)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	fflush(stdout);
	puts("[.] bytes object info");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = ((PyBytesObject *)(p))->ob_sval;

	printf("  size: %zd\n", size);

	if (size > 0)
	{
		printf("  trying string: %s\n", str);
		printf("  first %ld bytes: ", size <= 10 ? size + 1 : 10);
		for (i = 0; i <= size && i < 10; ++i)
			printf("%02x%s", (unsigned char)str[i], (i == size || i == 9) ? "" : " ");
		printf("\n");
	}
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to a PyObject (Python object)
 */
void print_python_float(PyObject *p)
{
	double value;
	const char *float_str;
	int precision;

	fflush(stdout);
	puts("[.] float object info");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);

	/*Convert the float to a string and determine precision*/
	float_str = PyOS_double_to_string(value, 'g', 16, Py_DTSF_ADD_DOT_0, NULL);
	precision = strchr(float_str, '.')
					? (int)(strlen(float_str) - (strchr(float_str, '.') - float_str) - 1)
					: 0;

	/*Print the float value with the exact number of decimal places*/
	printf("  value: %.*f\n", precision, value);
}

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to a PyObject (Python object)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	fflush(stdout);
	puts("[*] Python list info");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyListObject *)p)->ob_base.ob_size;
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);

		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);

		if (strcmp(item->ob_type->tp_name, "float") == 0)
			print_python_float(item);
	}
}
