#include "lists.h"
/**
*check_cycle - check if there is cycle in the singly linked list.
*@list: pointer to the head of the struct.
*Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *backward = list;
	listint_t *forward = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (forward && backward && backward->next)
	{
		forward = forward->next;
		backward = backward->next->next;
		if (forward == backward)
			return (1);
	}
	return (0);
}
