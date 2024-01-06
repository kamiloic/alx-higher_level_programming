#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * free_int_array - Frees memory allocated for an array of integers.
 * @array: Pointer to the array of integer pointers.
 * @len: Length of the array.
 */
void free_int_array(int **array, int len)
{
	int i;

	for (i = 0; i < len; i++)
		free(array[i]);

	free(array);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int **int_array = NULL;
	int i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (*head != NULL)
	{
		len += 1;
		int_array = realloc(int_array, len * sizeof(int *));
		int_array[len - 1] = &(*head)->n;
		*head = (*head)->next;
	}

	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (*int_array[i] != *int_array[j])
		{
			/* Free int_array */
			free_int_array(int_array, len);
			return (0);
		}
	}

	/* Free int_array */
	free_int_array(int_array, len);

	return (1);
}
