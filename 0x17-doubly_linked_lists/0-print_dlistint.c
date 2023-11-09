#include "lists.h"
/**
*print_dlistint - function that prints data of list(node).
*@h: pointer to head.
*Return: number of node
*
*/
size_t print_dlistint(const dlistint_t *h)
{
	int node = 0;
	const dlistint_t *temp = h;

	if (h == NULL)
		return (0);

	while (temp)
	{
		node += 1;
		printf("%d\n", temp->n);
		temp = temp->next;
	}

	return (node);

}
