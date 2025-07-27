#!/usr/bin/env python3
"""
Test Runner for Algorithm Exercises
Run tests for individual problems or entire categories
"""

import os
import sys
import subprocess
import time
from pathlib import Path

class TestRunner:
    def __init__(self):
        self.base_dir = Path("exercises")
        self.difficulties = ["beginner", "medium", "hard"]
    
    def run_single_test(self, difficulty, problem_num):
        """Run test for a single problem"""
        problem_file = self.base_dir / difficulty / f"problem_{problem_num:03d}.py"
        
        if not problem_file.exists():
            print(f"❌ Problem file not found: {problem_file}")
            return False
        
        print(f"🧪 Testing {difficulty} problem {problem_num}...")
        
        try:
            start_time = time.time()
            result = subprocess.run([sys.executable, str(problem_file)], 
                                  capture_output=True, text=True, timeout=30)
            end_time = time.time()
            
            if result.returncode == 0:
                print(f"✅ Test passed! ({end_time - start_time:.2f}s)")
                if result.stdout:
                    print(f"Output: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Test failed!")
                if result.stderr:
                    print(f"Error: {result.stderr.strip()}")
                return False
                
        except subprocess.TimeoutExpired:
            print("⏰ Test timed out (30s limit)")
            return False
        except Exception as e:
            print(f"💥 Error running test: {e}")
            return False
    
    def run_category_tests(self, difficulty, start=1, end=100):
        """Run tests for a category of problems"""
        print(f"\n🎯 Running {difficulty} tests (problems {start}-{end})")
        print("=" * 50)
        
        passed = 0
        failed = 0
        
        for i in range(start, end + 1):
            if self.run_single_test(difficulty, i):
                passed += 1
            else:
                failed += 1
            print()  # Empty line for readability
        
        print(f"📊 Results: {passed} passed, {failed} failed")
        return passed, failed
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Running all algorithm exercise tests...")
        total_passed = 0
        total_failed = 0
        
        for difficulty in self.difficulties:
            passed, failed = self.run_category_tests(difficulty)
            total_passed += passed
            total_failed += failed
        
        print("\n" + "=" * 50)
        print("🏁 FINAL RESULTS")
        print("=" * 50)
        print(f"✅ Total Passed: {total_passed}")
        print(f"❌ Total Failed: {total_failed}")
        print(f"📊 Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    
    def validate_problem_structure(self, difficulty, problem_num):
        """Validate that a problem file has the correct structure"""
        problem_file = self.base_dir / difficulty / f"problem_{problem_num:03d}.py"
        
        if not problem_file.exists():
            return False, "File does not exist"
        
        try:
            with open(problem_file, 'r') as f:
                content = f.read()
            
            # Check for required components
            required_components = [
                'def ',  # At least one function definition
                'def test_',  # Test function
                'if __name__ == "__main__":',  # Main block
                '"""',  # Docstring
            ]
            
            missing = []
            for component in required_components:
                if component not in content:
                    missing.append(component)
            
            if missing:
                return False, f"Missing components: {missing}"
            
            return True, "Structure is valid"
            
        except Exception as e:
            return False, f"Error reading file: {e}"

def main():
    runner = TestRunner()
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python test_runner.py single <difficulty> <problem_num>")
        print("  python test_runner.py category <difficulty> [start] [end]")
        print("  python test_runner.py all")
        print("  python test_runner.py validate <difficulty> <problem_num>")
        return
    
    command = sys.argv[1]
    
    if command == "single":
        if len(sys.argv) >= 4:
            difficulty = sys.argv[2]
            problem_num = int(sys.argv[3])
            runner.run_single_test(difficulty, problem_num)
        else:
            print("Usage: python test_runner.py single <difficulty> <problem_num>")
    
    elif command == "category":
        if len(sys.argv) >= 3:
            difficulty = sys.argv[2]
            start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
            end = int(sys.argv[4]) if len(sys.argv) > 4 else 100
            runner.run_category_tests(difficulty, start, end)
        else:
            print("Usage: python test_runner.py category <difficulty> [start] [end]")
    
    elif command == "all":
        runner.run_all_tests()
    
    elif command == "validate":
        if len(sys.argv) >= 4:
            difficulty = sys.argv[2]
            problem_num = int(sys.argv[3])
            is_valid, message = runner.validate_problem_structure(difficulty, problem_num)
            if is_valid:
                print(f"✅ {message}")
            else:
                print(f"❌ {message}")
        else:
            print("Usage: python test_runner.py validate <difficulty> <problem_num>")
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
