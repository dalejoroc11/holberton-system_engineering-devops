#include "holberton.h"
/**
 * fun_printf_s - print strings and %
 * @*s: pointer
 * Return: Always 0
 */
int fun_printf_s(char *s)
	{
	    int i;
	    if (s == '\0')
	      s = "(null)";
	    for (i = 0; s[i] != '\0'; i++)
	    {
	        _putchar(s[i]);
	    }
	    return (i);
	}
