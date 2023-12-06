#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * check_cycle - checks for cycles in a link list
 * @list: the loops a cycle makes
 * Return: 1 if success or 0 on failure
*/
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
