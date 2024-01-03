#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the beginning of linked list
 * @number: value of n
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curent = *head;
	unsigned int i = 0;

	if (!(curent) || (*curent).n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;

		return (*head);
	}

	while (curent)
	{
		if (!((*curent).next) || (*curent).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			(*new).n = number;
			(*new).next = (*curent).next;
			(*curent).next = new;
			return (new);
		}
		curent = (*curent).next;
		i++;
	}

	return (NULL);
}
