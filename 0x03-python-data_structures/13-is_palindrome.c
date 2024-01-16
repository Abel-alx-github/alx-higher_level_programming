#include "lists.h"
/**
*is_palindrome - function that check if the list is palindrom.
*@head: pointer to pointer of first head.
*Return: 1 if list is palindrome otherwise 0
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *temp = *head;
	int j, i, count_node = 0;

	while (temp)
	{
		count_node++;
		temp = temp->next;
	}
	int arr[count_node];

	temp = *head;
	i = count_node - 1;

	while (i >= 0)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i -= 1;
	}
	temp = *head;
	j = 0;

	while (j < count_node)
	{
		if (arr[j] == temp->n)
		{
			temp = temp->next;
		}
		else
			return (0);
		j += 1;
	}
	return (1);

}
