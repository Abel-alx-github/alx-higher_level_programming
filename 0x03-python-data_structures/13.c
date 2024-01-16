#include "lists.h"

int is_palindrome(listint_t **head)
{
	if(head == NULL && (*head)->next)
		return (1);
	listint_t *current = *head;
	listint_t *pre = NULL;
	listint_t *next = *head;

	while(current->next)
	{
		next = next->next;
		current->next = pre;
		pre = current;
		current = next;
	}
	listint_t *from_head = *head;
	current->next = pre;
	pre = NULL;
	printf("%d and ", pre->n);
	while(current->next)
	{
		if (current->n == from_head->n)
		{
			current = current->next;
			from_head = from_head->next;
		}
		else
			return (0);
	}
	return (1);
}
