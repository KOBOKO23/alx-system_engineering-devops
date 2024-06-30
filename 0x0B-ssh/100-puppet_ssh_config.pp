file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host 100.26.217.251\n" +
             "    IdentityFile ~/.ssh/school\n" +
             "    PasswordAuthentication no\n",
}
