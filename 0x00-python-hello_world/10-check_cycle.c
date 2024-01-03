#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 otherwise.
 *
 * Description: Uses the Floyd's cycle-finding algorithm to
 * check if a singly linked list has a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return 0;

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return 1; /* Cycle found */

		slow = slow->next;
		fast = fast->next->next;
	}

	return 0; /* No cycle found */
}
