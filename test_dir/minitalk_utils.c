/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   minitalk_utils.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/15 13:30:56 by midbella          #+#    #+#             */
/*   Updated: 2024/01/15 13:36:43 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_atoi(const char *str)
{
	int	i;
	int	result;
	int	sign;

	i = 0;
	result = 0;
	sign = 1;
	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 13))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] && str[i] >= '0' && str[i] <= '9')
	{
		result *= 10;
		result += str[i] - 48;
		i++;
	}
	return (result * sign);
}

int	ft_print_s(const char *str)
{
	int	i;
	int	tot;

	tot = 0;
	i = 0;
	if (str == NULL)
	{
		tot = write(1, "(null)", 6);
		return (tot);
	}
	while (str[i])
	{
		tot += write (1, &str[i], 1);
		i++;
	}
	return (tot);
}

int	ft_print_d(int nb)
{
	long	n;
	char	s[10];
	int		j;
	int		tot;

	tot = 0;
	n = nb;
	if (n < 0)
	{
		tot += write(1, "-", 1);
		n = n * -1;
	}
	j = 0;
	while (n >= 10)
	{
		s[j] = (n % 10) + 48;
		n = n / 10;
		j++;
	}
	s[j] = n + 48;
	while (j >= 0)
		tot += write(1, &s[j--], 1);
	return (tot);
}
