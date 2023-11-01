#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 **insert_node - insert data in sorted list
 *@head: pointer to pointer to first list
 *@number: data to be added
 *Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	current = *head;
	new->n = number;
	new->next = NULL;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
