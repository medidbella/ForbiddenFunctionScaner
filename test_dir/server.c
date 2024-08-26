/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: midbella <midbella@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/01/14 19:14:47 by midbella          #+#    #+#             */
/*   Updated: 2024/01/15 14:45:25 by midbella         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

short *block;

void	handler(int sig)
{
	*(char *)block = *(char *)block << 1 | (sig == SIGUSR1);
	*(char *)(block + 1) += 1;
	if (*(char *)((block + 1)) == 8)
	{
		write(1, (char *)block, 1);
		*(char *)((block + 1)) = 0;
	}
}

int	main(void)
{
	short g;
	g = 0;
	block = &g;
	signal(SIGUSR1, handler);
	signal(SIGUSR2, handler);
	ft_print_s("THE PROCESS ID OF THE SERVER => ");
	ft_print_d(getpid()); 
	ft_print_s(" <=\n");
	while (1)
	{
	}
}
