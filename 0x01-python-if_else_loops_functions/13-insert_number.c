#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
/**
 * insert_node - adds a nummber to a list
 * @head: pointer to main head of list
 * @number: number to be added
 * Return: address of the inserted node return NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
	listint_t *prevList = NULL;
	listint_t *currentList = *head;

	if (!newNode)
	{
		return (NULL);
	}
	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	while (currentList && currentList->n < number)
	{
		prevList = currentList;
		currentList = currentList->next;
	}
	if (currentList == *head)
	{
		*head = newNode;
	}
	else
	{
		prevList->next = newNode;
	}
	newNode->next = currentList;
	return (newNode);
}
