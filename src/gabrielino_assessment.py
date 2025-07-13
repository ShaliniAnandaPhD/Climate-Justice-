"""
Main Gabrielino Assessment orchestrator class.
"""

import asyncio
import time
from typing import Dict, Any

from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn

from .utils.console_utils import console, create_header_panel, clear_screen
from .agents import (
    PerilScorerEngine,
    ContextualFairnessAuditor, 
    HistoricalDataSynthesisEngine,
    MultiFactorRiskOrchestrator
)
from .visualizations import ASCIIChartGenerator
from .data import FIRE_SCENARIO, DEMOGRAPHIC_DATA
from config.settings import PROJECT_NAME, APP_VERSION, DEFAULT_CLAIM_ADDRESS, DEFAULT_CLAIM_DAMAGE


class GabrielinoAssessment:
    """Orchestrates the entire assessment workflow."""
    
    def __init__(self):
        self.claim_address = ""
        self.claim_damage = 0
        self.claim_demographic = ""
        self.chart_generator = ASCIIChartGenerator()

    def clear_screen(self):
        """Clear the console screen."""
        clear_screen()

    def print_header(self):
        """Print the application header."""
        header_title = f"🔥 {PROJECT_NAME.upper()} FIRE ASSESSMENT v{APP_VERSION} 🔥"
        sub_header = "A Multi-Agent AI System for Fair & Efficient Claims Processing"
        
        header_panel = create_header_panel(header_title, sub_header)
        console.print(header_panel)

    def show_architecture_diagram(self):
        """Display a simplified architecture overview."""
        console.print("[bright_blue]🏗️ GABRIELINO ARCHITECTURE OVERVIEW 🏗️[/bright_blue]")
        console.print("[bright_blue]" + "="*50 + "[/bright_blue]")
        console.print("[white]Multi-Agent System for Insurance Claims[/white]")
        console.print()
        console.print("[green]✅ 4 Specialized Agents:[/green]")
        console.print("   🔥 PerilScorerEngine - Real-time fire data analysis")
        console.print("   ⚖️ ContextualFairnessAuditor - AI bias detection")
        console.print("   📚 HistoricalDataSynthesisEngine - Pattern analysis")
        console.print("   🎯 MultiFactorRiskOrchestrator - Decision synthesis")
        console.print()
        console.print("[green]✅ Key Benefits:[/green]")
        console.print("   ⚡ 360x Faster than Traditional Review")
        console.print("   💰 99.8% Cost Reduction")
        console.print("   🎯 94% Accuracy vs 82% Traditional")
        console.print("   ⚖️ AI-Powered Bias Detection")
        console.print("[bright_blue]" + "="*50 + "[/bright_blue]")

    def get_user_input(self):
        """Get claim details interactively from the user."""
        console.print(Panel(
            "[bold cyan]STEP 1: Interactive Claim Intake[/bold cyan]", 
            border_style="cyan", 
            padding=(1, 2)
        ))
        
        self.claim_address = Prompt.ask(
            "[bold]Enter the property address[/bold]", 
            default=DEFAULT_CLAIM_ADDRESS
        )
        
        self.claim_damage = IntPrompt.ask(
            "[bold]Enter the estimated damage amount ($)[/bold]", 
            default=DEFAULT_CLAIM_DAMAGE
        )
        
        is_low_income = Confirm.ask(
            "[bold]Is the claimant from a low-income demographic?[/bold]", 
            default=True
        )
        
        if is_low_income:
            self.claim_demographic = "low_income"
        else:
            self.claim_demographic = "high_income"
        
        console.print("\n[green]✅ Claim details received. System is ready to proceed.[/green]")

    async def run_analysis(self):
        """Run the enhanced analysis with comprehensive visualizations."""
        self.clear_screen()
        self.print_header()
        
        console.print(Panel(
            "[bold]Enhanced Multi-Agent Analysis: Performance, Cost & Critical Assessment[/bold]", 
            style="white", 
            border_style="blue"
        ))
        
        console.print(f"Analyzing claim for [bold]{self.claim_address}[/] | Damage: [bold]${self.claim_damage:,.0f}[/]")
        console.print("Running high-performance parallel workflow with comprehensive analysis...")

        # Run parallel agent processing
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task("Running parallel agent workflow...", total=None)
            par_start_time = time.time()
            
            # Create and run parallel tasks
            parallel_tasks = [
                PerilScorerEngine().assess(FIRE_SCENARIO),
                ContextualFairnessAuditor().assess(self.claim_demographic, FIRE_SCENARIO),
                HistoricalDataSynthesisEngine().assess(self.claim_damage)
            ]
            
            parallel_results = await asyncio.gather(*parallel_tasks)
            
            # Map results by agent name
            name_to_key_map = {
                "PerilScorerEngine": "fire",
                "ContextualFairnessAuditor": "bias",
                "HistoricalDataSynthesisEngine": "memory"
            }
            par_agent_results = {name_to_key_map[res['agent_name']]: res for res in parallel_results}
            
            # Run orchestration
            decision_res = await MultiFactorRiskOrchestrator().synthesize(par_agent_results, self.claim_damage)
            par_total_time = (time.time() - par_start_time) * 1000

        all_results = list(par_agent_results.values())
        all_results.append(decision_res)
        
        # Calculate total cost
        total_cost = sum(res.get("cost", 0.0) for res in all_results)
        
        # Show performance analysis
        console.print("\n[bold magenta]📊 PERFORMANCE ANALYSIS[/bold magenta]")
        self._show_performance_summary(par_total_time, total_cost)
        
        console.print("\n[dim]Press Enter to view cost analysis...[/dim]")
        input()
        
        # Show cost analysis
        console.print("\n[bold yellow]💰 COST ANALYSIS[/bold yellow]")
        self._show_cost_analysis(total_cost)
        
        console.print("\n[dim]Press Enter to view critical assessment...[/dim]")
        input()
        
        # Show critical assessment
        console.print("\n[bold red]🚨 CRITICAL ASSESSMENT[/bold red]")
        fire_risk = par_agent_results['fire']['fire_risk_score']
        bias_score = par_agent_results['bias']['bias_score']
        self._show_critical_assessment(decision_res, fire_risk, bias_score)
        
        console.print("\n[dim]Press Enter to view final recommendation...[/dim]")
        input()
        
        # Show final recommendation
        console.print("\n[bold magenta]📋 FINAL RECOMMENDATION[/bold magenta]")
        self._show_final_recommendation(decision_res)

    def _show_performance_summary(self, processing_time: float, total_cost: float):
        """Show performance comparison summary."""
        # Performance data for comparison
        performance_data = [
            ("Multi-Agent AI", processing_time, "🤖", "green"),
            ("Traditional Review", 432000, "👨‍💼", "red"),
            ("Pure API Workflow", 8500, "🔌", "yellow"),
            ("Simple Rules", 1200, "📏", "blue")
        ]
        
        chart = self.chart_generator.create_horizontal_bar_chart(
            performance_data, 
            title="Processing Time Comparison",
            show_values=True
        )
        console.print(chart)
        
        # Calculate improvements
        traditional_time = 432000
        speedup = traditional_time / processing_time
        console.print(f"\n[bold green]⚡ {speedup:.0f}x FASTER than traditional review![/bold green]")

    def _show_cost_analysis(self, total_cost: float):
        """Show cost analysis comparison."""
        cost_data = [
            ("Traditional Adjuster", 150.00, "👨‍💼", "red"),
            ("Pure API Workflow", 0.05, "🔌", "blue"),
            ("Multi-Agent System", total_cost, "🤖", "green"),
            ("Simple Rules", 0.001, "📏", "cyan")
        ]
        
        chart = self.chart_generator.create_horizontal_bar_chart(
            cost_data,
            title="Cost per Claim Comparison ($)",
            show_values=True
        )
        console.print(chart)
        
        # Calculate savings
        traditional_cost = 150.00
        savings = traditional_cost - total_cost
        savings_pct = (savings / traditional_cost) * 100
        console.print(f"\n[bold green]💰 ${savings:.4f} savings ({savings_pct:.1f}% cost reduction)![/bold green]")

    def _show_critical_assessment(self, decision_result: Dict[str, Any], 
                                 fire_risk: int, bias_score: float):
        """Show critical assessment matrix."""
        priority = decision_result["final_recommendation"]["priority"]
        priority_score = decision_result["priority_score"]
        
        console.print("    ╔═══════════════════════════════════════════════════════════════╗")
        console.print("    ║                    CRITICAL ASSESSMENT MATRIX                ║")
        console.print("    ╠═══════════════════════════════════════════════════════════════╣")
        console.print("    ║                                                               ║")
        
        # Fire Risk Meter
        fire_bar = self.chart_generator.create_progress_bar(fire_risk, 100, 20, "red")
        console.print(f"    ║ 🔥 Fire Peril Risk    │ {fire_bar} │ {fire_risk}/100")
        
        # Bias Risk Meter  
        bias_bar = self.chart_generator.create_progress_bar(bias_score, 100, 20, "yellow")
        console.print(f"    ║ ⚖️ Bias Risk Factor   │ {bias_bar} │ {bias_score:.0f}/100")
        
        # Priority Score
        priority_color = "red" if priority == "CRITICAL" else "yellow" if priority == "HIGH" else "green"
        priority_bar = self.chart_generator.create_progress_bar(priority_score, 100, 20, priority_color)
        console.print(f"    ║ 🎯 Priority Score     │ {priority_bar} │ {priority_score:.0f}/100")
        
        console.print("    ║                                                               ║")
        
        # Current case positioning
        if priority_score >= 80:
            position = ">>> CRITICAL ZONE <<<"
            pos_color = "bold red"
        elif priority_score >= 65:
            position = ">>> HIGH PRIORITY <<<"
            pos_color = "bold yellow"
        else:
            position = ">>> STANDARD TRACK <<<"
            pos_color = "bold green"
        
        console.print(f"    ║ Current Case: [{pos_color}]{position}[/{pos_color}]")
        console.print("    ╚═══════════════════════════════════════════════════════════════╝")

    def _show_final_recommendation(self, decision_res: Dict[str, Any]):
        """Display the final recommendation."""
        recommendation = decision_res['final_recommendation']
        priority = recommendation['priority']
        title = recommendation['title']
        priority_score = decision_res['priority_score']
        
        # Create styled recommendation panel
        art_text = Text()
        
        if priority == "CRITICAL":
            header_style = "bold white on red"
            border_style = "bold red"
        elif priority == "HIGH":
            header_style = "bold black on yellow"
            border_style = "bold yellow"
        else:
            header_style = "bold white on green"
            border_style = "bold green"
        
        art_text.append("╔══════════════════════════════════════════════════════════════════════════════╗\n", style=border_style)
        art_text.append("║ ", style=border_style)
        
        if priority == "CRITICAL":
            art_text.append("🚨 EMERGENCY ASSESSMENT COMPLETE 🚨", style=header_style)
        elif priority == "HIGH":
            art_text.append("⚠️  PRIORITY ASSESSMENT COMPLETE ⚠️", style=header_style)
        else:
            art_text.append("✅ STANDARD ASSESSMENT COMPLETE ✅", style=header_style)
        
        art_text.append(" " * 20 + "║\n", style=border_style)
        art_text.append("╠════════════════════════════════════════════════════════════════════════════════╣\n", style=border_style)
        
        # Priority score visualization
        score_bar = "█" * int(priority_score / 5) + "░" * (20 - int(priority_score / 5))
        art_text.append("║ ", style=border_style)
        art_text.append(f"Priority Score: {priority_score:.1f}/100", style="cyan")
        art_text.append(f" │ {score_bar} ║\n", style=border_style)
        
        # Recommendation details
        art_text.append("╟────────────────────────────────────────────────────────────────────────────────╢\n", style=border_style)
        art_text.append("║ ", style=border_style)
        art_text.append(f"Recommendation: {title}", style="bold cyan")
        art_text.append(" " * (65 - len(title)) + "║\n", style=border_style)
        
        art_text.append("║ ", style=border_style)
        art_text.append(f"Priority Level: {priority}", style=f"bold {priority.lower()}")
        art_text.append(" " * (65 - len(priority)) + "║\n", style=border_style)
        
        # Summary
        art_text.append("╟────────────────────────────────────────────────────────────────────────────────╢\n", style=border_style)
        art_text.append("║ ", style=border_style)
        art_text.append("Summary:", style="bold cyan")
        art_text.append(" " * 70 + "║\n", style=border_style)
        
        # Word wrap summary
        summary = recommendation['summary']
        words = summary.split()
        current_line = ""
        for word in words:
            if len(current_line + word) <= 72:
                current_line += word + " "
            else:
                art_text.append("║ " + current_line.ljust(76) + "║\n", style=border_style)
                current_line = word + " "
        if current_line:
            art_text.append("║ " + current_line.ljust(76) + "║\n", style=border_style)
        
        # Action items
        art_text.append("╟────────────────────────────────────────────────────────────────────────────────╢\n", style=border_style)
        art_text.append("║ ", style=border_style)
        art_text.append("IMMEDIATE ACTION ITEMS:", style="bold cyan")
        art_text.append(" " * 54 + "║\n", style=border_style)
        
        for i, action in enumerate(recommendation['actions'], 1):
            art_text.append("║ ", style=border_style)
            art_text.append(f"{i}. {action}", style="white")
            padding = 76 - len(f"{i}. {action}")
            art_text.append(" " * max(0, padding) + "║\n", style=border_style)
        
        art_text.append("╚══════════════════════════════════════════════════════════════════════════════╝\n", style=border_style)
        
        console.print(art_text)
