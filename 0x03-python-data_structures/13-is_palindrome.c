#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * reverse_List - checks a list backwards
 * @head: first item on list
 * Return: last item
*/
listint_t* reverse_List(listint_t* head) {
    listint_t* foward = NULL;
    listint_t* current = head;
    listint_t* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = foward;
        foward = current;
        current = next;
    }

    return foward;
}
/**
 * is_palindrome- checks if a word is palindrome or not
 * @head: firstt item on the list
 * @Return: 1 if true or 0 if false
*/
int is_palindrome(listint_t **head)
{
	listint_t *turtle = *head;
	listint_t *hare = *head;
	listint_t *secondHalf, *prevOfSl = *head;
	int aPalindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (hare != NULL && hare->next != NULL)
		{
			hare = hare->next->next;
			prevOfSl = turtle;
			turtle = turtle->next;
		}
		if (hare != NULL)
		{
			turtle = turtle->next;
		}
		secondHalf = reverse_List(turtle);
		while (secondHalf != NULL)
		{
			if ((*head)->data != secondHalf->data)
			{
				aPalindrome = 0;
				break;
			}
			*head = (*head)->next;
			secondHalf = secondHalf->next;
			secondHalf = revese_List(secondHalf);
			prevOfSl->next = secondHalf;			
		}
		return aPalindrome;
	}
}