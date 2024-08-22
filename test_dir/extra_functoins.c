/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   extra_functoins.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/25 21:04:54 by midbella          #+#    #+#             */
/*   Updated: 2024/05/30 18:42:06 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "philo.h"

int	ft_atoi(char *str)
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

unsigned long	ft_get_time(void)
{
	struct timeval	curr;

	gettimeofday(&curr, NULL);
	return ((curr.tv_sec * 1000) + (curr.tv_usec / 1000));
}

void	ft_sleep(unsigned long time)
{
	unsigned long	start;

	start = ft_get_time();
	while (ft_get_time() - start < time)
		usleep(1);
	return ;
}

int	did_all_phlios_eat(t_data *ref)
{
	int	i;

	i = 0;
	if (ref->max_eat_times == -1)
		return (0);
	while (i < ref->philos_number)
	{
		if (ref->philos[i].meals_number < ref->max_eat_times)
			return (0);
		i++;
	}
	return (1);
}
