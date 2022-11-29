#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node
 * @head: head of singly linked list
 * @number: value in singly linked list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp = *head, *tmp2;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!tmp || tmp->n >= number)
	{
		new_node->next = tmp, *head = new_node;
		return (new_node);
	}

	tmp2 = tmp->next;
	while (tmp && tmp2 && (tmp2->n < number))
		tmp = tmp->next, tmp2 = tmp->next;

	tmp->next = new_node, new_node->next = tmp2;
	return (new_node);
}
