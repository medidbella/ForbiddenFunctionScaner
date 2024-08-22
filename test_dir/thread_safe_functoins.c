/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   thread_safe_functoins.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/29 15:23:43 by midbella          #+#    #+#             */
/*   Updated: 2024/05/31 19:10:08 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "philo.h"

void	my_increment(int *ptr)
{
	int		i;
	int		part;
	char	*devider;

	part = 0;
	i = 0;
	devider = (char *)ptr;
	while (part <= 3)
	{
		if (devider[part] + 1 == 0)
			part++;
		else
			break ;
	}
	i = part - 1;
	while (i >= 0)
		memset(&devider[i--], 0, 1);
	memset(&devider[part], devider[part] +1, 1);
}

void	set_variable(unsigned long	*dest, unsigned long valeu)
{
	int		part;
	char	*val_devider;
	char	*dest_devider;

	part = 0;
	val_devider = (char *)&valeu;
	dest_devider = (char *)dest;
	while (part <= 7)
	{
		memset(&dest_devider[part], val_devider[part], 1);
		part++;
	}
}

void	print_message(char *str, t_data *data, int id)
{
	pthread_mutex_lock(&data->print_guard);
	if (data->status == 0)
		printf(str, ft_get_time() - data->t0, id);
	pthread_mutex_unlock(&data->print_guard);
}

void	destroy_mutexes(t_data *ref)
{
	int	i;

	i = 0;
	while (i < ref->philos_number)
	{
		pthread_mutex_destroy(&ref->forks[i]);
		i++;
	}
	pthread_mutex_destroy(&ref->print_guard);
}
