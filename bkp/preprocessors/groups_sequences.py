def _extract_sequences(number_list):
  def register(first, last):
    if first == last:
      sequences.append([first])
    else:
      sequences.append([first, last])

  first = int(number_list[0])
  last = int(number_list[0])
  sequences = []

  for x in range(len(number_list)):
    if (last + 1) == int(number_list[x]):
      last = int(number_list[x])
      if x == len(number_list) - 1:
        register(first, last)
    elif ((last + 1) - first) > 0:
      if (x > 0): # Skip first execution
        register(first, last)
      first = int(number_list[x])
      last = int(number_list[x])
      if (x == len(number_list) - 1):
        register(first, last)

  return sequences

def _extract_groups(sequences):

  group  = []
  for sequence in sequences:
    if len(sequence) == 1:
      group.append(1)
    else:
      group.append(sequence[1] - sequence[0] + 1)
  return group

def insert_sequences_and_groups(draws, conn):
  for draw, numbers in draws.items():
    sequences = _extract_sequences(numbers)
    groups = _extract_groups(sequences)
    conn.execute("UPDATE LOTOFACIL SET SEQUENCES = '" + str(sequences) + "', GROUPS = '" + str(groups) + "' WHERE ID = " + str(draw))
  conn.commit()
