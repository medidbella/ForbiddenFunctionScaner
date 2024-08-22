/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   before_simulatoin.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/18 20:45:52 by midbella          #+#    #+#             */
/*   Updated: 2024/06/01 13:32:59 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "philo.h"

void	initialize_philos(t_data *ref)
{
	int	iter;

	iter = 0;
	while (iter < ref->philos_number)
	{
		if (iter == 0)
			ref->philos[iter].r_fork = &ref->forks[ref->philos_number - 1];
		else
			ref->philos[iter].r_fork = &ref->forks[iter - 1];
		ref->philos[iter].l_fork = &ref->forks[iter];
		ref->philos[iter].last_meal_time = ref->t0;
		ref->philos[iter].philo_number = iter + 1;
		pthread_mutex_init(&ref->forks[iter], NULL);
		ref->philos[iter].data = ref;
		ref->philos[iter].meals_number = 0;
		iter++;
	}
}

int	initialize_data(t_data *ref, char **av, int ac)
{
	ref->max_eat_times = -1;
	ref->t0 = ft_get_time();
	ref->philos_number = ft_atoi(av[1]);
	ref->life_time = ft_atoi(av[2]);
	ref->eat_time = ft_atoi(av[3]);
	ref->sleep_time = ft_atoi(av[4]);
	ref->status = 0;
	if (ac == 6)
		ref->max_eat_times = ft_atoi(av[5]);
	pthread_mutex_init(&ref->print_guard, NULL);
	ref->philos = malloc(sizeof(t_philo) * ref->philos_number);
	ref->forks = malloc(sizeof(pthread_mutex_t) * ref->philos_number);
	if (!ref->philos || !ref->forks)
		return (1);
	initialize_philos(ref);
	return (0);
}

int	check_args(int ac, char **av)
{
	int	s_index;
	int	c_index;

	s_index = 1;
	c_index = 0;
	if (ac < 5 || ac > 6)
		return (0);
	while (av[s_index])
	{
		c_index = 0;
		while (av[s_index][c_index])
		{
			if (!(av[s_index][c_index] >= '0' && av[s_index][c_index] <= '9'))
				return (0);
			c_index++;
		}
		s_index++;
	}
	return (1);
}
