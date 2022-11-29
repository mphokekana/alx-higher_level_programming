#include "lists.h"

/**
 * insert_node - Inserts a numberinto a sorted singly-linked list
 * @head: A pointer of the linked list
 * @number: The number to insert
 * Return: If the function falls - NULL, otherwise - a pointer to the new mode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->node = new;

	return (new);
}
