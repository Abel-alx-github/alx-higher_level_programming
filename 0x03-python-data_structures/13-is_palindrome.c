/**
*is_palindrome - function that check if the list is palindrom.
*@head: pointer to pointer of first head.
*Return: 1 if list is palindrome otherwise 0
*/
#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *current = *head;
	listint_t *forward = *head;
	listint_t *start = *head;
	int no_node = 0;

	while (current)
	{
		no_node++;
		current = current->next;
	}
	int mid = no_node / 2;
	int i = 0;
	int is_pal = 0;

	while (i <= mid)
	{
		if (forward == NULL)
			forward = *head;
		int j = 1;

		while (forward)
		{
			if (j == no_node)
			{
				if (start->n == forward->n)
					is_pal++;
			}
			j++;
			forward = forward->next;
		}
		free_listint(forward);
		start = start->next;
		i++, no_node--, j = 1;
	}
	if (i == is_pal)
		return (1);
	return (0);

}
