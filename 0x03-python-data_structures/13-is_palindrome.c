#include "lists.h"
/**
*is_palindrome - function that check if the list is palindrom.
*@head: pointer to pointer of first head.
*Return: 1 if list is palindrome otherwise 0
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *current = *head;
	listint_t *reversed_head = NULL;

	while (current != NULL)
	{
		listint_t *next;

		next = current->next;
		current->next = reversed_head;
		reversed_head = current;
		current = next;
	}

	listint_t *original_head;
	listint_t *reversed;

	original_head = *head;
	reversed = reversed_head;

	while (original_head != NULL && reversed != NULL)
	{
		if (original_head->n != reversed->n)
		{
			return (0);
		}
		original_head = original_head->next;
		reversed = reversed->next;
	}
	return (1);
}

