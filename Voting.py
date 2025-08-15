class Vote():
    def __init__(self):
        self.__candidates = []
        self.__votes = {}

    def getCandidates(self):
        return self.__candidates
    
    def addCandidate(self, newCandidate):
        if not newCandidate.strip():
            return 'Candidate name cannot be empty!\n'
        
        if newCandidate in self.__candidates:
            return f'{newCandidate} already exists in the Candidates!\n'
        else:
            self.__candidates.append(newCandidate)
            return f'{newCandidate} has been added successfully!\n'


    def candidateIndex(self, candidate):
        for i in range(len(self.__candidates)):
            if candidate == self.__candidates[i]:
                return i
        return -1

    def removeCandidate(self, candidate):
        index = self.candidateIndex(candidate)
        if index == -1:
            return 'No candidate with this name!\n'
        if index in self.__votes:  
            print(f'{candidate} has votes! are you sure you want to remove this candidate?\nY - N\n')
            while True:
                choice = input().upper()
                if choice == 'N':
                    print(f'Removal of {candidate} cancelled.\n')
                    break
                elif choice == 'Y':
                    self.__candidates.remove(candidate)
                    del self.__votes[index]
                    print(f'{candidate} has been removed successfully!\n')
                    break
                else:
                    print('Invalid choice! Please enter Y or N.')
        else:
            self.__candidates.remove(candidate)
            return f'{candidate} has been removed successfully!\n'


    def vote_to(self, candidate, NumOfVotes):
        if NumOfVotes < 0:
            return 'Number of votes cannot be negative!\n'
        
        index = self.candidateIndex(candidate)
        if index == -1:
            return 'This is not a candidate!\n'

        if index in self.__votes:
            self.__votes[index] += NumOfVotes
        else:
            self.__votes[index] = NumOfVotes
        
        return f'Successfully added {NumOfVotes} votes to {candidate}.\n'

    def displayWinner(self):
        if not self.__votes:
            return 'No votes Yet!\n'
        
        MaxVote = max(self.__votes.values())
        winners = []
        for index, votes in self.__votes.items():
            if votes == MaxVote:
                winners.append(self.__candidates[index])
        
        if len(winners) == 1:
            return(f"Winner: {winners[0]} with {MaxVote} votes")
        else:
            winners_str = ", ".join(winners)
            return (f"Tie between: {winners_str} (each with {MaxVote} votes)")
    
def voting():
    system = Vote()
    print("-------------------- HI, it's time to vote! --------------------\n")
    while (True):
        choice = input("1. Add a candidate\n2. Remove Candidate\n3. Vote\n4. Show your winner!\n5. Exit\nChoice: ")
        match choice:
            case '1':
                candidate = input('\nAdd a candidate: ')
                print(f'{system.addCandidate(candidate)}')     
            case '2':
                candidate = input('\nRemove a candidate: ')
                print(f'{system.removeCandidate(candidate)}')
            case '3':
                candidate = input('\n Who do you want to vote for? ')
                if system.candidateIndex(candidate) == -1:
                    print(f'{candidate} doesn\'t exist!\n')
                    continue
                votes = int(input(f'\n How many voted for {candidate}? '))
                system.vote_to(candidate,votes)
            case '4':
                print(f'{system.displayWinner()}')
            case '5':
                break
            case _:
                print('\nPlease enter a valid choice!\n')
    print("-------------------- THANK YOU FOR VOTING! --------------------\n")
        

if __name__ == "__main__" :
    voting()


