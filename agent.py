import json
import random
from constants import (
    Action,
    ALPHA,
    GAMMA,
    EPSILON,
    EPSILON_MIN,
    EPSILON_DECAY
)


class Agent:
    """A simple Q-learning agent for the Slither game."""

    def __init__(self, learning=True):
        """Initialize the agent with empty Q-table."""
        self.q_table = {}
        self.alpha = ALPHA
        self.gamma = GAMMA
        self.epsilon = EPSILON
        self.epsilon_min = EPSILON_MIN
        self.epsilon_decay = EPSILON_DECAY
        self.learning = learning

    def choose_action(self, state):
        """Choose action using epsilon-greedy policy."""
        if not self.learning:
            q_values = self._get_q_values(state)
            return max(q_values, key=q_values.get)

        if random.random() < self.epsilon:
            action = random.choice(list(Action))
        else:
            q_values = self._get_q_values(state)
            action = max(q_values, key=q_values.get)
        self.epsilon = max(
            self.epsilon_min,
            self.epsilon * self.epsilon_decay
        )
        return action

    def update(self, state, action, reward, next_state):
        """Update Q-table using Bellman equation."""
        if not self.learning:
            return
        q_values = self._get_q_values(state)
        q_next = self._get_q_values(next_state)

        target = reward + self.gamma * max(q_next.values())
        q_values[action] = (
            q_values[action]
            + self.alpha * (target - q_values[action])
        )

    def save(self, filepath):
        """Save the Q-table to a file."""
        serializable = {}
        for state, actions in self.q_table.items():
            state_key = str(state)
            serializable[state_key] = {
                action.name: value
                for action, value in actions.items()
            }
            with open(filepath, 'w') as f:
                json.dump(serializable, f, indent=2)

    def load(self, filepath):
        """Load the Q-table from a file."""
        with open(filepath, 'r') as f:
            serializable = json.load(f)
        self.q_table = {}
        for state_key, actions in serializable.items():
            state = eval(state_key)
            self.q_table[state] = {
                Action[action_name]: value
                for action_name, value in actions.items()
            }

    def _get_q_values(self, state):
        """Return Q-values for all actions in the given state."""
        if state not in self.q_table:
            self.q_table[state] = {
                action: 0.0 for action in Action
            }
        return self.q_table[state]
