#!/usr/bin/env python3
"""
Progress Tracker for Algorithm Exercises
Track your progress across all 300 exercises
"""

import os
import json
from datetime import datetime

class ProgressTracker:
    def __init__(self):
        self.progress_file = "progress.json"
        self.load_progress()
    
    def load_progress(self):
        """Load progress from file"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                "beginner": {},
                "medium": {},
                "hard": {},
                "stats": {
                    "total_completed": 0,
                    "beginner_completed": 0,
                    "medium_completed": 0,
                    "hard_completed": 0,
                    "start_date": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat()
                }
            }
    
    def save_progress(self):
        """Save progress to file"""
        self.progress["stats"]["last_updated"] = datetime.now().isoformat()
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def mark_completed(self, difficulty, problem_num, time_taken=None):
        """Mark a problem as completed"""
        problem_key = f"problem_{problem_num:03d}"
        self.progress[difficulty][problem_key] = {
            "completed": True,
            "completion_date": datetime.now().isoformat(),
            "time_taken": time_taken
        }
        
        # Update stats
        self.update_stats()
        self.save_progress()
        print(f"✅ Marked {difficulty} problem {problem_num} as completed!")
    
    def update_stats(self):
        """Update completion statistics"""
        beginner_count = len([p for p in self.progress["beginner"].values() if p.get("completed")])
        medium_count = len([p for p in self.progress["medium"].values() if p.get("completed")])
        hard_count = len([p for p in self.progress["hard"].values() if p.get("completed")])
        
        self.progress["stats"]["beginner_completed"] = beginner_count
        self.progress["stats"]["medium_completed"] = medium_count
        self.progress["stats"]["hard_completed"] = hard_count
        self.progress["stats"]["total_completed"] = beginner_count + medium_count + hard_count
    
    def show_progress(self):
        """Display current progress"""
        stats = self.progress["stats"]
        print("\n" + "="*50)
        print("🎯 ALGORITHM EXERCISES PROGRESS")
        print("="*50)
        print(f"📊 Total Progress: {stats['total_completed']}/300 ({stats['total_completed']/300*100:.1f}%)")
        print(f"🟢 Beginner: {stats['beginner_completed']}/100 ({stats['beginner_completed']}%)")
        print(f"🟡 Medium: {stats['medium_completed']}/100 ({stats['medium_completed']}%)")
        print(f"🔴 Hard: {stats['hard_completed']}/100 ({stats['hard_completed']}%)")
        print(f"📅 Started: {stats['start_date'][:10]}")
        print(f"🕒 Last Updated: {stats['last_updated'][:10]}")
        print("="*50)
        
        # Progress bars
        self.show_progress_bar("Beginner", stats['beginner_completed'], 100, "🟢")
        self.show_progress_bar("Medium", stats['medium_completed'], 100, "🟡")
        self.show_progress_bar("Hard", stats['hard_completed'], 100, "🔴")
    
    def show_progress_bar(self, label, completed, total, emoji):
        """Show a progress bar"""
        percentage = completed / total
        bar_length = 30
        filled_length = int(bar_length * percentage)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"{emoji} {label:8} [{bar}] {completed:3d}/{total} ({percentage*100:5.1f}%)")
    
    def list_next_problems(self, difficulty="all", count=5):
        """List next problems to solve"""
        print(f"\n📝 Next {count} problems to solve:")
        
        difficulties = ["beginner", "medium", "hard"] if difficulty == "all" else [difficulty]
        
        for diff in difficulties:
            print(f"\n{diff.upper()}:")
            completed_problems = set(self.progress[diff].keys())
            
            for i in range(1, 101):
                problem_key = f"problem_{i:03d}"
                if problem_key not in completed_problems:
                    print(f"  • Problem {i:03d}: exercises/{diff}/{problem_key}.py")
                    count -= 1
                    if count <= 0:
                        return

def main():
    tracker = ProgressTracker()
    
    if len(os.sys.argv) > 1:
        command = os.sys.argv[1]
        
        if command == "show":
            tracker.show_progress()
        elif command == "complete":
            if len(os.sys.argv) >= 4:
                difficulty = os.sys.argv[2]
                problem_num = int(os.sys.argv[3])
                tracker.mark_completed(difficulty, problem_num)
            else:
                print("Usage: python progress_tracker.py complete <difficulty> <problem_num>")
        elif command == "next":
            difficulty = os.sys.argv[2] if len(os.sys.argv) > 2 else "all"
            count = int(os.sys.argv[3]) if len(os.sys.argv) > 3 else 5
            tracker.list_next_problems(difficulty, count)
        else:
            print("Available commands: show, complete, next")
    else:
        tracker.show_progress()

if __name__ == "__main__":
    main()
