/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   philo_main.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/25 20:50:48 by midbella          #+#    #+#             */
/*   Updated: 2024/06/02 14:46:15 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "philo.h"

void	repititve_meal(t_philo *ref)
{
	pthread_mutex_lock(ref->l_fork);
	print_message("%lu\t%d has taken a fork\n", ref->data, ref->philo_number);
	pthread_mutex_lock(ref->r_fork);
	print_message("%lu\t%d has taken a fork\n", ref->data, ref->philo_number);
	print_message("%lu\t%d is eating\n", ref->data, ref->philo_number);
	set_variable(&ref->last_meal_time, ft_get_time());
	my_increment(&ref->meals_number);
	ft_sleep(ref->data->eat_time);
	pthread_mutex_unlock(ref->r_fork);
	pthread_mutex_unlock(ref->l_fork);
	return ;
}

void	thread_function(t_philo *ref)
{
	int	state;

	state = 1;
	if ((ref->philo_number % 2 == 0) || (ref->data->philos_number % 2 != 0
			&& ref->philo_number == ref->data->philos_number
			&& ref->data->philos_number != 1))
	{
		print_message("%lu\t%d is thinking\n", ref->data, ref->philo_number);
		ft_sleep(ref->data->eat_time - 5);
		state = 0;
	}
	while (1)
	{
		if (state == 1)
			print_message("%lu\t%d is thinking\n", ref->data,
				ref->philo_number);
		repititve_meal(ref);
		print_message("%lu\t%d is sleeping\n", ref->data, ref->philo_number);
		ft_sleep(ref->data->sleep_time);
		state = 1;
	}
	return ;
}

void	monitoring(t_data *ref)
{
	int	i;

	i = 0;
	while (!did_all_phlios_eat(ref))
	{
		if (ft_get_time() - ref->philos[i].last_meal_time > ref->life_time)
		{
			memset(&ref->status, 1, 1);
			printf("%lu\t%d died\n", ft_get_time() - ref->t0,
				ref->philos[i].philo_number);
			return ;
		}
		i++;
		if (i == ref->philos_number)
		{
			usleep(50);
			i = 0;
		}
	}
	memset(&ref->status, 1, 1);
	return ;
}

int	start_threads(t_data *data, int size)
{
	int			i;
	pthread_t	monitor;

	i = 0;
	while (i < size)
	{
		if (pthread_create(&(data->philos[i].thread), NULL,
				(void *)thread_function, &data->philos[i]))
			return (1);
		i++;
	}
	if (pthread_create(&monitor, NULL, (void *)monitoring, data) != 0)
		return (1);
	i = 0;
	while (i < size)
	{
		if (pthread_detach(data->philos[i].thread))
			return (1);
		i++;
		if (i == size && pthread_join(monitor, NULL) != 0)
			return (1);
	}
	return (0);
}

int	main(int ac, char **av)
{
	t_data		data;

	if (!check_args(ac, av))
		return (1);
	if (initialize_data(&data, av, ac) == 1)
		return (1);
	if (data.max_eat_times == 0 || data.philos_number == 0)
		return (0);
	if (start_threads(&data, data.philos_number) == 1)
		return (1);
	destroy_mutexes(&data);
	free(data.philos);
	free(data.forks);
	return (0);
}
