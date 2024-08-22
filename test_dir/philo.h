/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   philo.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/25 20:50:44 by midbella          #+#    #+#             */
/*   Updated: 2024/06/01 12:17:47 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PHILO_H 
# define PHILO_H

# include <stdio.h>
# include <pthread.h>
# include <stdlib.h>
# include <string.h>
# include <unistd.h>
# include <sys/time.h>

typedef struct s_data	t_data;

typedef struct s_philo
{
	pthread_t		thread;
	unsigned long	last_meal_time;
	int				philo_number;
	int				meals_number;
	pthread_mutex_t	*r_fork;
	pthread_mutex_t	*l_fork;
	t_data			*data;
}	t_philo;

typedef struct s_data
{
	t_philo			*philos;
	int				philos_number;
	unsigned long	life_time;
	int				eat_time;
	int				sleep_time;
	int				max_eat_times;
	int				status;
	pthread_mutex_t	print_guard;
	pthread_mutex_t	*forks;
	unsigned long	t0;
}	t_data;

int				check_args(int ac, char **av);
int				ft_atoi(char *str);
int				initialize_data(t_data *ref, char **av, int ac);
void			initialize_philos(t_data *ref);
void			thread_function(t_philo *ref);
int				check_args(int ac, char **av);
void			ft_sleep(unsigned long time);
unsigned long	ft_get_time(void);
int				ft_atoi(char *str);
void			destroy_mutexes(t_data *ref);
void			print_message(char *str, t_data *data, int id);
int				did_all_phlios_eat(t_data *ref);
void			my_increment(int *val);
void			set_variable(unsigned long	*dest, unsigned long valeu);

#endif