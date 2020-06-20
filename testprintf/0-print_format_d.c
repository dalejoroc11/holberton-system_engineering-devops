#include "holberton.h"
/**
*fun_printf_num - function print numbers
*@num: variable number
*@len: lenght number
*Return: counter
*/
int fun_printf_num(unsigned int num, int len)
{
	if (num / 10)/*ifnumberdivten*/
		len = fun_printf_num(num / 10, len);/*lenght number*/
	_putchar(num % 10 + '0');/*print num*/
	return (len + 1);/*counter that return*/
}
