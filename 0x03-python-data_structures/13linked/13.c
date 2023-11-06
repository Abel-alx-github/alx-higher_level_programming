#include "lists.h"

/**int is_palindrome(listint_t **head)
{
	if (head == NULL || (*head)->next == NULL)
		return (1);
	else
	{
		listint_t *current = *head;
		reverse(**head);
		while (current)
		{
			if (current->n != (*head)->n)
			{
				current = current->next;
				*head = *head->next;
			}
			else
				return (0);

		}
	}
	return (1);
}

void *reverse(listint_t **head)
{

	listint_t *next = NULL;
	listint_t *pre = NULL;
	listint_t *temp = *head;

	while (temp->next)
	{
		next = temp->next;
		temp->next = pre;
		pre = temp;
		temp = next;
	}
	*head = pre;
	

}*/
int is_palindrome(listint_t **head) {
  // Check if the list is empty.
  if (*head == NULL) {
    return 1;
  }

  // Reverse the linked list.
  listint_t *reversed_head = NULL;
  listint_t *current = *head;
  while (current != NULL) {
    listint_t *next = current->next;
    current->next = reversed_head;
    reversed_head = current;
    current = next;
  }

  // Compare the original linked list to the reversed linked list.
  listint_t *original_node = *head;
  listint_t *reversed_node = reversed_head;
  while (original_node != NULL && reversed_node != NULL) {
    if (original_node->n != reversed_node->n) {
      return 0;
    }
    original_node = original_node->next;
    reversed_node = reversed_node->next;
  }

  // If we reach the end of both linked lists without finding any differences,
  // then the original linked list is a palindrome.
  return 1;
}
