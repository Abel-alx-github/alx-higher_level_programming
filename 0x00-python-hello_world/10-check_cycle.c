#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t **cycle = &list;
	int i;

	for (i = 0; cycle; i++)
	{
		if ((*cycle)[i]->next == ((*cycle)[i + 1]->next))
			return (1);
		*cycle = cycle->next;
	}
	return (0);

}
